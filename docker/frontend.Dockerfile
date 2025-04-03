FROM node:17
WORKDIR /app

COPY bebopshed/frontend/package.json ./
RUN npm install

WORKDIR /app/bebopshed/frontend
CMD ["npm", "run", "dev"]
