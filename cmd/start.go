/*
Copyright © 2024 NAME HERE <EMAIL ADDRESS>
*/
package cmd

import (

	//"path/filepath"

	"github.com/spf13/cobra"
)

// Make a function to check the available sites.

// startCmd represents the start command
var startCmd = &cobra.Command{
	Use:   "start",
	Short: "It will start a localhost server.",
	Long:  `This commnad is used to start the local server for the several websites`,
	Run: func(cmd *cobra.Command, args []string) {
		// now first display the menue ..
		//fmt.Println("\033[31;1m Our websites list will be here")
		// now make a function to check the available sites.
		//isAvl("site")
		// now make a regx function to extract the line with input field ..
		//checkInp("site_path")// this function will return the input field's variables so we can host that page

	},
}

func init() {
	rootCmd.AddCommand(startCmd)

	// Here you will define your flags and configuration settings.

	// Cobra supports Persistent Flags which will work for this command
	// and all subcommands, e.g.:
	// startCmd.PersistentFlags().String("foo", "", "A help for foo")

	// Cobra supports local flags which will only run when this command
	// is called directly, e.g.:
	// startCmd.Flags().BoolP("toggle", "t", false, "Help message for toggle")
}
