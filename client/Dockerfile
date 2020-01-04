
# USE NODE ALPINE AS THE BASE IMAGE
# TAG IMAGE AS BUILDER - SINCE WE ARE BUILDING THE BUILD FILE
FROM node:alpine as builder

# CREATE A WORKING DIRECTORY 
# Do we need this path now?
WORKDIR /opt/www/client

# COPY PACKAGE JSON INTO WORK DIR
COPY frontend/package.json .

# INSTALL DEPENDENCIES
RUN npm install

# COPY THE REST OF THE FOLDER TO TAKE ADVANTAGE OF LAYER CACHING
COPY frontend .

RUN npm run build

# USE NGNIX IMAGE
# SERVE THE BUILD FOLDER
FROM nginx
EXPOSE 3000
COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf
COPY --from=builder /opt/www/client/build /usr/share/nginx/html