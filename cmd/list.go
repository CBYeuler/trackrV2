// TODO: implement list command
package cmd

import (
	"database/sql"
	"fmt"

	"github.com/CBYeuler/trackr/db"
	"github.com/spf13/cobra"
)

var listCmd = &cobra.Command{
	Use:   "list",
	Short: "List all saved logs",
	RunE: func(cmd *cobra.Command, args []string) error {
		dbConn, err := db.OpenDB()
		if err != nil {
			return fmt.Errorf("failed to open DB: %w", err)
		}
		defer dbConn.Close()

		rows, err := dbConn.Query(`SELECT category, value, created_at FROM logs ORDER BY created_at DESC`)
		if err != nil {
			return fmt.Errorf("query failed: %w", err)
		}
		defer rows.Close()

		for rows.Next() {
			var category, value string
			var createdAt sql.NullString
			if err := rows.Scan(&category, &value, &createdAt); err != nil {
				return err
			}
			fmt.Printf("[%s] %s  (%s)\n", category, value, createdAt.String)
		}
		return rows.Err()
	},
}

func init() {
	rootCmd.AddCommand(listCmd)
}
