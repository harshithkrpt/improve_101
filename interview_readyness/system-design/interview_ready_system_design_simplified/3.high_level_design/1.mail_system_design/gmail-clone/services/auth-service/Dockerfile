FROM node:16-alpine
WORKDIR /app
COPY package.json package-lock.json ./
RUN yarn install --production
COPY . .
CMD ["node", "src/index.js"]
