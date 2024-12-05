/*
Copyright © 2024 NAME HERE <EMAIL ADDRESS>
*/
package cmd

import (
	"fmt"
	"os"
	"path/filepath"

	"github.com/spf13/cobra"
)

// Make a function to check the available sites.
func isAvl(path string site string) (bool,filePath string) {
	// now check if folder is available ..
	_,err:=os.Stat(path)
	if err!=nil{
		fmt.Println("\033[31;1m Some required file has been removed, please run git pull into your terminal and run the script again..")
		os.Exit(1)
	}
return true, "path/sites"
}
// Make function to check the inp field so we can host the page and get the variable ..
func checkInp(site string) []string{

// this function will return a slice of string with inp variable..
fmt.Println("write your login for the extract the inp field.")
rerutn ["whoami","hostname"]
}

// startCmd represents the start command
var startCmd = &cobra.Command{
	Use:   "start",
	Short: "It will start a localhost server.",
	Long:  `This commnad is used to start the local server for the several websites`,
	Run: func(cmd *cobra.Command, args []string) {
		// now first display the menue ..
		fmt.Println("\033[31;1m Our websites list will be here")
		// now make a function to check the available sites.
		isAvl("site")
		// now make a regx function to extract the line with input field ..
		checkInp("site_path")// this function will return the input field's variables so we can host that page 

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
