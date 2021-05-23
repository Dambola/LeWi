FROM node:14-alpine3.10 as builder

WORKDIR /app

COPY . .

RUN npm install -g @quasar/cli cross-env
RUN npm install
RUN cross-env API_URL=http://localhost:8390 quasar build

FROM nginx:1.19.10

WORKDIR /usr/share/nginx/html

RUN rm /etc/nginx/conf.d/default.conf

COPY nginx.conf /etc/nginx/conf.d/
COPY --from=builder /app/dist/spa .

ENTRYPOINT ["nginx", "-g", "daemon off;"]