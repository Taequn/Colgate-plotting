library(tidyverse)
library(jsonlite)
test <- read_csv("all_data.csv")

reply <- fromJSON("Database/199901.json",
         simplifyDataFrame = T)

full.df <- NULL

# for(json in list.files("Database")){
#   parse <- fromJSON(paste("Database/",json,sep=""),
#                     simplifyDataFrame = T)
# 
#   full.df <- bind_rows(full.df, parse$data)
# }

full.df <- fromJSON("Database/199901.json",
                    simplifyDataFrame = T)

full.df <- full.df$data

facVec <- full.df$faculty
testdf <- data.frame(facVec[1])

tempVec <- c()

for(x in facVec){
  if(length(x)!=0){
    tempVec <- c(as.character(data.frame(x)["displayName"]), tempVec)
  }
  else{
    tempVec <- c(NA, tempVec)
  }
}

full.df.clean <- bind_cols(full.df, as.vector(tempVec))

buildings <- full.df.clean$meetingsFaculty
testdf$meetingTime["buildingDescription"]

vector.of.buildings <- c()



for(x in buildings){
  if(is.null(data.frame(x)$meetingTime$buildingDescription)){
    x <- NA
  }else{
    x <- data.frame(x)$meetingTime$buildingDescription
    if(length(x)>1){
      x <- x[1]
    }
  }
  vector.of.buildings<-c(vector.of.buildings, x)
}

full.df.clean <- bind_cols(full.df, as.vector(vector.of.buildings))

