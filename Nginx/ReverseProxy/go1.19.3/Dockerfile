FROM golang:1.19.3

WORKDIR /usr/src/app

COPY main.go ./

RUN go build -o /usr/local/bin/app ./main.go

EXPOSE 8000

CMD ["app"]
