# Use a Node image to build the Vue app
FROM node:22 AS builder

WORKDIR /app

# Copy package.json and install dependencies
COPY package.json package-lock.json ./
RUN npm install

# Copy the rest of the project and build
COPY . .
RUN npm run build

# Use a lightweight server for the built files
FROM nginx:alpine

# Copy built files to Nginx's public folder
COPY --from=builder /app/dist /usr/share/nginx/html

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]
