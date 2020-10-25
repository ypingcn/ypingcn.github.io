package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"os"
	"strings"
	"time"

	sitemap "github.com/snabb/sitemap"
)

const (
	URL_PREFIX = "https://ypingcn.github.io/notes/"
	FILE_SUFIX = ".md"
)

func isVaild(name string) bool {
	return strings.HasSuffix(name, FILE_SUFIX)
}

func genURL(dir string, name string) string {
	fileName := strings.TrimSuffix(name, FILE_SUFIX)
	if fileName == "index" {
		return URL_PREFIX + dir + "/"
	} else {
		return URL_PREFIX + dir + "/" + fileName + "/"

	}

}
func main() {
	sm := sitemap.New()
	now := time.Unix(time.Now().Unix(), 0).UTC()
	files, err := ioutil.ReadDir("./")
	if err != nil {
		log.Fatal("ioutil.ReadDir err - [", err, "]")
	}
	for _, file := range files {
		name := file.Name()
		if file.IsDir() {
			filesInDir, err := ioutil.ReadDir("./" + name + "/")
			if err != nil {
				log.Fatal("ioutil.ReadDir err - [", err, "]")
			}
			for _, fileInDir := range filesInDir {
				if !fileInDir.IsDir() && isVaild(fileInDir.Name()) {
					URL := genURL(name, fileInDir.Name())
					sm.Add(&sitemap.URL{
						Loc:        URL,
						LastMod:    &now,
						ChangeFreq: sitemap.Daily,
					})
				}
			}
		}
	}
	sitemapFile, err := os.OpenFile("./sitemap.xml", os.O_RDWR, 0666)
	if err != nil {
		fmt.Println(err)
	}
	sm.WriteTo(sitemapFile)
}
