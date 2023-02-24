FROM golang:1.19.3

WORKDIR /usr/src/app

COPY uds-over-tcp ./uds-over-tcp
COPY uds-over-udp ./uds-over-udp
COPY uds-over-http ./uds-over-http
COPY uds-over-grpc ./uds-over-grpc

RUN go build -o /usr/local/bin/uds-over-tcp-server ./uds-over-tcp/server/main.go
RUN go build -o /usr/local/bin/uds-over-tcp-client ./uds-over-tcp/client/main.go

CMD ["uds-over-tcp-server"]