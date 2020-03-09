# Version: 0.0.1
FROM alpine:latest
RUN apk add --no-cache git bash
RUN apk add --no-cache nodejs nodejs-npm
RUN apk upgrade --no-cache --available
RUN npm config set unsafe-perm true
RUN npm install -g @angular/cli npm-snapshot
RUN npm cache clean --force
