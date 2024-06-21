CREATE TABLE api_keys (
    id INTEGER PRIMARY KEY,
    api_key TEXT NOT NULL DEFAULT 'DEFAULT',
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id)
);
