FROM node:14-alpine3.10 as builder

WORKDIR /app

COPY . .

ENV API_URL=${API_URL}

RUN npm install -g @quasar/cli cross-env
RUN npm install
RUN cross-env API_URL=${API_URL} quasar build

FROM nginx:1.19.10


WORKDIR /usr/share/nginx/html

RUN rm /etc/nginx/conf.d/default.conf

COPY nginx.conf /etc/nginx/conf.d/
COPY --from=builder /app/dist/spa .

ENTRYPOINT ["nginx", "-g", "daemon off;"]