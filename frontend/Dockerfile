
# USE NODE ALPINE AS THE BASE IMAGE
# TAG IMAGE AS BUILDER - SINCE WE ARE BUILDING THE BUILD FILE
FROM node:alpine as builder
WORKDIR '/app'
COPY package*.json ./
RUN npm install
COPY . .
# CREATE THE BUILD FOLDER
RUN npm run build

# USE NGNIX IMAGE
# SERVE THE BUILD FOLDER
FROM nginx
EXPOSE 80
COPY --from=builder /app/build /usr/share/nginx/html