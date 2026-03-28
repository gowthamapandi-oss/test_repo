import subprocess
import yaml
import pickle
import hashlib
import sqlite3

# ── SECRETS ──────────────────────────────────────────────────────────────────
# semgrep p/secrets: detected-private-key
PRIVATE_KEY = """-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEA2a2rwplBQLzHPZe5RJr9tjpVmqBMBLSNMOyLcETcgHDoNLBF
-----END RSA PRIVATE KEY-----"""

# ── SAST: subprocess shell injection ─────────────────────────────────────────
# semgrep: python.lang.security.audit.subprocess-shell-true
def run_command(cmd):
    subprocess.call(cmd, shell=True)

# ── SAST: unsafe yaml.load deserialization ────────────────────────────────────
# semgrep: python.lang.security.deserialization.pickle.avoid-pyyaml-load
def parse_config(data):
    return yaml.load(data)

# ── SAST: pickle deserialization ──────────────────────────────────────────────
# semgrep: python.lang.security.deserialization.pickle.avoid-pickle
def load_object(data):
    return pickle.loads(data)

# ── SAST: md5 used for password hashing ──────────────────────────────────────
# semgrep: python.lang.security.audit.md5-used-as-password
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

# ── SAST: SQL injection via string concatenation ──────────────────────────────
# semgrep: python.sqlalchemy.security.sqlalchemy-execute-raw-query
def get_user(user_id):
    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = " + user_id)
    return cursor.fetchall()

# ── SAST: eval on user input ──────────────────────────────────────────────────
# semgrep: python.lang.security.audit.eval-detected
def calculate(expression):
    return eval(expression)
