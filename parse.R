library(tidyverse)
library(jsonlite)

full.df <- NULL

for(json in list.files("Database")){
  parse <- fromJSON(paste("Database/",json,sep=""),
                    simplifyDataFrame = T)

  full.df <- bind_rows(full.df, parse$data)
}

facVec <- full.df$faculty
testdf <- data.frame(facVec[1])

tempVec <- c()

for(x in facVec){
  if(length(x)!=0){
    tempVec <- c(tempVec, as.character(data.frame(x)["displayName"]))
  }
  else{
    tempVec <- c(tempVec, NA)
  }
}

full.df.clean <- bind_cols(full.df, as.vector(tempVec))
full.df.clean <- full.df.clean%>%
  mutate(names = ...35)

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

full.df.clean <- bind_cols(full.df.clean, as.vector(vector.of.buildings))

full.df.clean <- full.df.clean%>%
  mutate(buildingName = ...37)

full.df.clean.final <- full.df.clean %>% mutate(faculty = NULL,
                         meetingsFaculty = NULL,
                         ...35 = NULL,
                         ...37 = NULL,
                         reservedSeatSummary=NULL)

write_csv(full.df.clean.final, "parsed_data.csv")

view(full.df.clean.final)

  
