CREATE TABLE links (
    url TEXT NOT NULL,
    title TEXT,
    class_id INTEGER NOT NULL,
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    FOREIGN KEY (class_id) REFERENCES classes(id)
);
CREATE TABLE classes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    class_name TEXT NOT NULL,
    class_description TEXT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);


