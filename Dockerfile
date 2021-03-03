# Use the latest node lts on Alpine
FROM node:lts-alpine3.12
LABEL org.opencontainers.image.source https://github.com/spaceflightnewsapi/spaceflightnewsapi

# Copy all the data over
COPY . .

# Install all packages from the package.json
# Build the admin interface in production mode
RUN yarn install && NODE_ENV=production yarn run build

# No explenation needed
EXPOSE 1337
CMD [ "yarn", "start" ]
