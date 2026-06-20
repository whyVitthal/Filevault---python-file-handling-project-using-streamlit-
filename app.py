import streamlit as st
from pathlib import Path
import os

# ── Page Config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="FileVault – File Manager",
    page_icon="🗂️",
    layout="centered",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* ── gradient hero ── */
.hero {
    background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 50%, #a855f7 100%);
    border-radius: 18px;
    padding: 2.2rem 2rem 1.8rem;
    margin-bottom: 2rem;
    text-align: center;
    color: white;
    box-shadow: 0 8px 32px rgba(99,102,241,0.3);
}
.hero h1 { font-size: 2.4rem; font-weight: 700; margin: 0 0 .3rem; letter-spacing: -1px; }
.hero p  { font-size: 1rem; opacity: .85; margin: 0; }

/* ── op cards ── */
.op-card {
    background: white;
    border: 1.5px solid #e0e7ff;
    border-radius: 14px;
    padding: 1.4rem 1.6rem;
    margin-bottom: 1.2rem;
    box-shadow: 0 2px 12px rgba(99,102,241,.07);
}

/* ── status badges ── */
.badge-success {
    background: #dcfce7; color: #166534;
    border: 1px solid #86efac;
    border-radius: 8px; padding: .5rem 1rem;
    font-weight: 600; font-size: .9rem; display: inline-block;
}
.badge-error {
    background: #fee2e2; color: #991b1b;
    border: 1px solid #fca5a5;
    border-radius: 8px; padding: .5rem 1rem;
    font-weight: 600; font-size: .9rem; display: inline-block;
}
.badge-info {
    background: #ede9fe; color: #5b21b6;
    border: 1px solid #c4b5fd;
    border-radius: 8px; padding: .5rem 1rem;
    font-weight: 600; font-size: .9rem; display: inline-block;
}

/* ── sidebar ── */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #1e1b4b 0%, #312e81 100%);
    color: white;
}
[data-testid="stSidebar"] * { color: white !important; }
[data-testid="stSidebar"] .stSelectbox label { font-weight: 600; font-size: 1rem; }

/* ── input styling ── */
.stTextInput > div > input, .stTextArea > div > textarea {
    border-radius: 10px !important;
    border: 1.5px solid #e0e7ff !important;
    font-family: 'Inter', sans-serif !important;
}
.stTextInput > div > input:focus, .stTextArea > div > textarea:focus {
    border-color: #6366f1 !important;
    box-shadow: 0 0 0 3px rgba(99,102,241,.15) !important;
}

/* ── buttons ── */
.stButton > button {
    background: linear-gradient(135deg, #6366f1, #8b5cf6) !important;
    color: white !important;
    border: none !important;
    border-radius: 10px !important;
    font-weight: 600 !important;
    padding: .55rem 1.6rem !important;
    font-size: .95rem !important;
    transition: all .2s ease !important;
}
.stButton > button:hover {
    transform: translateY(-1px) !important;
    box-shadow: 0 6px 18px rgba(99,102,241,.35) !important;
}

/* ── file list ── */
.file-chip {
    display: inline-block;
    background: #ede9fe;
    color: #5b21b6;
    border-radius: 20px;
    padding: .2rem .85rem;
    margin: .25rem .2rem;
    font-size: .85rem;
    font-weight: 500;
}

/* ── section titles ── */
.section-title {
    font-size: 1.1rem; font-weight: 700;
    color: #3730a3; margin-bottom: .7rem;
}
</style>
""", unsafe_allow_html=True)

# ── Helpers ───────────────────────────────────────────────────────────────────
WORK_DIR = Path("FileVault_files")
WORK_DIR.mkdir(exist_ok=True)

def safe_path(name: str) -> Path:
    return WORK_DIR / name

def list_files():
    return sorted([f.name for f in WORK_DIR.iterdir() if f.is_file()])

def ok(msg):  st.markdown(f'<div class="badge-success">✅ {msg}</div>', unsafe_allow_html=True)
def err(msg): st.markdown(f'<div class="badge-error">❌ {msg}</div>', unsafe_allow_html=True)
def info(msg):st.markdown(f'<div class="badge-info">ℹ️ {msg}</div>', unsafe_allow_html=True)

# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <h1>🗂️ FileVault</h1>
  <p>A clean Python-powered File Manager · Create · Read · Update · Delete</p>
</div>
""", unsafe_allow_html=True)

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## ⚙️ Operation")
    operation = st.selectbox(
        "Choose an operation",
        ["📄 Create File", "📖 Read File", "✏️ Update File", "🗑️ Delete File"],
        label_visibility="collapsed"
    )
    st.markdown("---")
    st.markdown("### 📁 Existing Files")
    files = list_files()
    if files:
        for f in files:
            st.markdown(f'<span class="file-chip">📄 {f}</span>', unsafe_allow_html=True)
    else:
        st.markdown("*No files yet — create one!*")
    st.markdown("---")
    st.caption("Built with Python + Streamlit")

# ═══════════════════════════════════════════════════════════════════════════════
#  CREATE
# ═══════════════════════════════════════════════════════════════════════════════
if operation == "📄 Create File":
    st.markdown('<div class="section-title">📄 Create a New File</div>', unsafe_allow_html=True)
    with st.container():
        filename = st.text_input("File Name", placeholder="e.g. notes.txt")
        content  = st.text_area("File Content", placeholder="Type what you want to write…", height=160)
        if st.button("Create File"):
            if not filename.strip():
                err("Please enter a file name.")
            else:
                path = safe_path(filename.strip())
                if path.exists():
                    err("A file with that name already exists!")
                else:
                    try:
                        path.write_text("\n" + content)
                        ok(f"'{filename}' created successfully!")
                        st.rerun()
                    except Exception as e:
                        err(f"Error: {e}")

# ═══════════════════════════════════════════════════════════════════════════════
#  READ
# ═══════════════════════════════════════════════════════════════════════════════
elif operation == "📖 Read File":
    st.markdown('<div class="section-title">📖 Read a File</div>', unsafe_allow_html=True)
    files = list_files()
    if not files:
        info("No files found. Create a file first.")
    else:
        filename = st.selectbox("Select File to Read", files)
        if st.button("Read File"):
            path = safe_path(filename)
            try:
                text = path.read_text()
                st.markdown("**📄 File Contents:**")
                st.code(text if text.strip() else "(empty file)", language="")
                st.caption(f"Size: {path.stat().st_size} bytes")
            except Exception as e:
                err(f"Error: {e}")

# ═══════════════════════════════════════════════════════════════════════════════
#  UPDATE
# ═══════════════════════════════════════════════════════════════════════════════
elif operation == "✏️ Update File":
    st.markdown('<div class="section-title">✏️ Update a File</div>', unsafe_allow_html=True)
    files = list_files()
    if not files:
        info("No files found. Create a file first.")
    else:
        filename = st.selectbox("Select File to Update", files)
        action   = st.radio(
            "What would you like to do?",
            ["📝 Rename", "➕ Append Content", "🔄 Overwrite Content"],
            horizontal=True
        )

        if action == "📝 Rename":
            new_name = st.text_input("New File Name", placeholder="e.g. renamed_notes.txt")
            if st.button("Rename File"):
                if not new_name.strip():
                    err("Please enter a new file name.")
                else:
                    old_path = safe_path(filename)
                    new_path = safe_path(new_name.strip())
                    if new_path.exists():
                        err("A file with that name already exists!")
                    else:
                        try:
                            old_path.rename(new_path)
                            ok(f"Renamed to '{new_name}' successfully!")
                            st.rerun()
                        except Exception as e:
                            err(f"Error: {e}")

        elif action == "➕ Append Content":
            append_data = st.text_area("Content to Append", height=130)
            if st.button("Append to File"):
                try:
                    with open(safe_path(filename), "a") as fa:
                        fa.write("\n" + append_data)
                    ok("Content appended successfully!")
                except Exception as e:
                    err(f"Error: {e}")

        elif action == "🔄 Overwrite Content":
            new_data = st.text_area("New Content (will replace existing)", height=130)
            if st.button("Overwrite File"):
                try:
                    safe_path(filename).write_text("\n" + new_data)
                    ok("File overwritten successfully!")
                except Exception as e:
                    err(f"Error: {e}")

# ═══════════════════════════════════════════════════════════════════════════════
#  DELETE
# ═══════════════════════════════════════════════════════════════════════════════
elif operation == "🗑️ Delete File":
    st.markdown('<div class="section-title">🗑️ Delete a File</div>', unsafe_allow_html=True)
    files = list_files()
    if not files:
        info("No files found. Nothing to delete.")
    else:
        filename = st.selectbox("Select File to Delete", files)
        st.warning(f"⚠️ You are about to permanently delete **{filename}**. This cannot be undone.")
        col1, col2 = st.columns([1, 3])
        with col1:
            if st.button("🗑️ Delete"):
                path = safe_path(filename)
                try:
                    path.unlink()
                    ok(f"'{filename}' deleted successfully!")
                    st.rerun()
                except Exception as e:
                    err(f"Error: {e}")

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown(
    "<center><sub>FileVault · Built with 🐍 Python & Streamlit · "
    "File handling project by Vitthal</sub></center>",
    unsafe_allow_html=True
)