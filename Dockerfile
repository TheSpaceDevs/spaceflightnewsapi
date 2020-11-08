# Use the latest node lts on Alpine
FROM node:lts-alpine3.12

# Copy all the data over
COPY . .

# Install all packages from the package.json
RUN yarn install

# Build the admin interface in production mode
RUN NODE_ENV=production yarn run build

# No explenation needed
EXPOSE 1337
CMD [ "yarn", "start" ]
