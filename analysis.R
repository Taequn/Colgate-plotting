library(tidyverse)
library(DescTools)

dat <- read_csv("parsed_data.csv")


counting <- dat %>% group_by(names)%>%
  summarise(
    numOfClasses = n()
  )%>%
  filter(!is.na(names))%>%
  arrange(numOfClasses)


for(x in 0:10){
  print(counting[nrow(counting)-x,])
}

view(dat[which(dat$names=="NAME"),])
