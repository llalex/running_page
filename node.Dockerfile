FROM node:14  AS develop-node
WORKDIR /root/running_page
COPY ./package.json /root/running_page/package.json
COPY ./yarn.lock /root/running_page/yarn.lock
RUN npm config set registry https://registry.npm.taobao.org \
        && yarn install
