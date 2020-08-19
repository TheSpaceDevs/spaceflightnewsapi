# Use the latest node lts on Alpine
FROM node:lts-alpine3.12

# Copy all the data over
COPY . .

# Install all packages from the package.json
RUN npm ci --only=production

# Build the admin interface in production mode
RUN NODE_ENV=production npm run build

# No explenation needed
EXPOSE 1337
CMD [ "npm", "start" ]
