FROM node:16-alpine
# Installing libvips-dev for sharp Compatibility
RUN apk update && apk add  build-base gcc autoconf automake zlib-dev libpng-dev nasm bash vips-dev

ENV NODE_ENV=development
ENV PATH /app/node_modules/.bin:$PATH

USER node
WORKDIR /app

COPY --chown=node:node ./ .
RUN npm install
RUN npm run build

EXPOSE 1337

CMD ["npm", "run", "develop"]
