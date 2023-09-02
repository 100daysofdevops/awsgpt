import streamlit as st
import subprocess
import sqlite3
import tempfile
import os
import pickle
from pathlib import Path
import streamlit_authenticator as stauth


# --- USER AUTHENTICATION ---
names = ["Admin user"]
usernames = ["admin"]

# load hashed passwords
file_path = Path(__file__).parent / "hashed_password_file.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
    "awsgpt_dashboard", "abcdef", cookie_expiry_days=30)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Username/password is incorrect")

if authentication_status == None:
    st.warning("Please enter your username and password")

if authentication_status:
    # Initialize database
    conn = sqlite3.connect('search_history.db')
    c = conn.cursor()

    # Create table if it doesn't exist
    try:
        c.execute("CREATE TABLE IF NOT EXISTS history (search TEXT)")
        conn.commit()
    except sqlite3.OperationalError as e:
        st.error(f"Database Error: {e}")

    def run_awsgpt(prompt, request_type):
        try:
            process = subprocess.Popen(
                ["python3", "awsgpt.py"],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            stdout, stderr = process.communicate(input=f"{prompt}\n{request_type}")

            if process.returncode == 0:
                return stdout, None
            else:
                return None, stderr or "Unknown error occurred while generating code."
        except Exception as e:
            return None, str(e)

    def save_search_to_db(search_term):
        try:
            c.execute("INSERT INTO history (search) VALUES (?)", (search_term,))
            conn.commit()
        except sqlite3.OperationalError as e:
            st.error(f"Database Error: {e}")

    st.title('AWS GPT Assistant 🛠️')

    if 'generated_code' not in st.session_state:
        st.session_state.generated_code = ""

    user_prompt = st.text_area("📝 Enter your query:", "", height=200)
    selected_operation = st.selectbox("Choose operation:", ["Generate Code", "Generate Search"])

    if st.button("🚀 Run Operation"):
        generated_output, error = run_awsgpt(user_prompt, selected_operation)
        save_search_to_db(user_prompt)

        if error:
            st.error(f"❌ An error occurred: {error}")
        else:
            st.success("✅ Operation completed successfully!")
            if selected_operation == "Generate Code":
                st.session_state.generated_code = generated_output
                st.code(generated_output, language="python")
            else:
                st.markdown(generated_output, unsafe_allow_html=True)

    if selected_operation == "Generate Code":
        if st.button("🔍 Execute Generated Code"):
            try:
                with tempfile.NamedTemporaryFile(suffix=".py", delete=False, mode='w') as temp:
                    temp.write(st.session_state.generated_code)
                    temp_path = temp.name

                exec_result = subprocess.run(["python3", temp_path], capture_output=True, text=True)

                if exec_result.returncode != 0:
                    st.subheader("🔴 Execution Errors")
                    st.code(exec_result.stderr, language="plain")
                else:
                    st.subheader("🟢 Execution Output")
                    st.code(exec_result.stdout or "No standard output produced.", language="plain")
            except Exception as e:
                st.error(f"❌ Error executing code: {e}")
            finally:
                if 'temp_path' in locals():
                    os.remove(temp_path)

    if st.button("📜 Show Previous Searches"):
        try:
            c.execute("SELECT * FROM history")
            rows = c.fetchall()
            if rows:
                st.markdown("### Previous Searches 📜")
                list_items = ""
                for row in rows:
                    list_items += f"<li style='margin: 4px; padding: 4px; font-weight: bold;'>{row[0]}</li>"
                full_list = f"<ul>{list_items}</ul>"
                st.markdown(full_list, unsafe_allow_html=True)
            else:
                st.info("No previous searches found.")
        except sqlite3.OperationalError as e:
            st.error(f"Database Error: {e}")
    authenticator.logout("Logout", "sidebar")
    st.sidebar.title(f"Welcome {name}")
    conn.close()
# Footer section
st.markdown(
    """
    ---
    #### Contact Information
    If you want to contact, you can reach out to [Prashant Lakhera via LinkedIn](https://www.linkedin.com/in/prashant-lakhera-696119b/).
    """,
    unsafe_allow_html=True,
)    
