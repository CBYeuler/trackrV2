package db

import (
	"database/sql"

	_ "modernc.org/sqlite" // pure-Go SQLite driver (no CGO)
)

// OpenDB opens (or creates) the SQLite database and ensures
// the 'logs' table exists.
func OpenDB() (*sql.DB, error) {
	db, err := sql.Open("sqlite", "tracker.db")
	if err != nil {
		return nil, err
	}

	// Create the table if it doesn't exist
	_, err = db.Exec(`
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT NOT NULL,
            value TEXT NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        );
    `)
	if err != nil {
		return nil, err
	}

	return db, nil
}

// InsertLog inserts a new log entry into the database.
func InsertLog(db *sql.DB, category string, value string) error {
	_, err := db.Exec(
		"INSERT INTO logs (category, value) VALUES (?, ?)",
		category, value,
	)
	return err
}

// CloseDB closes the database connection safely.
func CloseDB(db *sql.DB) error {
	if db != nil {
		return db.Close()
	}
	return nil
}

// GetLogs retrieves all logs from the database.
func GetLogs(db *sql.DB) ([]string, error) {
	rows, err := db.Query("SELECT category || ': ' || value FROM logs ORDER BY created_at DESC")
	if err != nil {
		return nil, err
	}
	defer rows.Close()

	var logs []string
	for rows.Next() {
		var log string
		if err := rows.Scan(&log); err != nil {
			return nil, err
		}
		logs = append(logs, log)
	}
	return logs, nil
}

// Task represents a task in the tracker.
// It contains the task name and other relevant fields.
// This struct is used to define the structure of tasks in the database.
