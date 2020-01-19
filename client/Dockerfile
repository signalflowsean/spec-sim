
# USE NODE ALPINE AS THE BASE IMAGE
# TAG IMAGE AS BUILDER - SINCE WE ARE BUILDING THE BUILD FILE
FROM node:alpine as builder

# CREATE A WORKING DIRECTORY 
WORKDIR '/app'

# COPY PACKAGE JSON INTO WORK DIR
COPY client/package.json .

# INSTALL DEPENDENCIES
RUN npm install

# COPY THE REST OF THE FOLDER TO TAKE ADVANTAGE OF LAYER CACHING
COPY client .

RUN npm run build

# USE NGNIX IMAGE
# SERVE THE BUILD FOLDER
FROM nginx
EXPOSE 3000
COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf
COPY --from=builder /app/build /usr/share/nginx/html