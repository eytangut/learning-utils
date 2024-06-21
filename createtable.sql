CREATE TABLE user_classes (
    user_id INTEGER,
    class_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (class_id) REFERENCES classes(id)
);


