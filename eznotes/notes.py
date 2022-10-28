from .db import get_conn_and_cur


def get_all_notes(sort_by, order):
    cur = get_conn_and_cur()[1]
    if sort_by == "alphabetical":
        sort_by = "title"
    cur.execute(f"SELECT * FROM notes ORDER BY {sort_by} {order}")
    return cur.fetchall()


def get_full_note(note_id):
    cur = get_conn_and_cur()[1]

    cur.execute(f"SELECT * FROM notes WHERE id like '{note_id}%'")
    note = cur.fetchone()
    return f"{note[1]}\n{note[2]}"


def note_exists(note_id):
    cur = get_conn_and_cur()[1]
    cur.execute(f"SELECT * FROM notes WHERE id LIKE '{note_id}%'")
    if not cur.fetchone():
        return False
    return True


def add_note_to_db(text):
    from .db import insert

    title, body = get_title_and_body(text)

    insert((title, body), text)


def get_note_title(note_id):
    cur = get_conn_and_cur()[1]
    cur.execute(f"SELECT title FROM notes WHERE id LIKE '{note_id}%'")
    return cur.fetchone()


def get_note_body(note_id):
    cur = get_conn_and_cur()[1]
    cur.execute(f"SELECT body FROM notes WHERE id LIKE '{note_id}%'")
    return cur.fetchone()


def get_title_and_body(note_text):
    return note_text.split("\n")[0].strip(), "\n".join(note_text.split("\n")[1:])


def get_note_date_created(note_id):
    cur = get_conn_and_cur()[1]
    cur.execute(f"SELECT date_created FROM notes WHERE id LIKE '{note_id}%'")
    return cur.fetchone()


def get_note_date_modified(note_id):
    cur = get_conn_and_cur()[1]
    cur.execute(f"SELECT date_modified FROM notes WHERE id LIKE '{note_id}%'")
    return cur.fetchone()
