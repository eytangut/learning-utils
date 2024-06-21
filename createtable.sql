CREATE TABLE mail (
    mail TEXT NOT NULL,
    user_id INTEGER,
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    FOREIGN KEY (user_id) REFERENCES users(id)

);


