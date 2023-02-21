FROM golang:1.19.3

WORKDIR /usr/src/echo

COPY server ./server
COPY client ./client

RUN go build -o /usr/local/bin/echo-server ./server/main.go
RUN go build -o /usr/local/bin/echo-client ./client/main.go


WORKDIR /usr/src/http-server
COPY http-server ./http-server

RUN go build -o /usr/local/bin/http-server ./http-server/main.go

CMD ["http-server"]
