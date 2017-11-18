# teemq

`teemq` pipes stdin to stdout and AMQP broker. It's also additionally buffers data
in an internal queue to never stop input stream and be resilient to AMQP broker
unavailabilty.

## Examples

    linegen | teemq --url amqp://guest:guest@rabbit:5672 --exchange logs --queue lines --key staging --declare > local.stream.txt

This will send stream of data from [linegen](https://github.com/dzeban/linegen)
to the stdout and also duplicate the data to the AMQP broker at host "rabbit",
sending it to the queue "lines" with a routing key "logs". Queue will be
declared if it's not existing (`--declare` option).

`teemq` can also connect to the RabbitMQ cluster by providing multiple hosts in
URL

    linegen \
    | teemq \
        --url 'amqp://user:pass@rabbit1:5672;amqp://user:pass@rabbit2:5672;amqp://user:pass@rabbit3:5672' \
        --exchange logs
        --queue etl \
        --key prod \
    > local.stream.txt

## Buffering

If the AMQP broker is not available `teemq` will buffer lines in the internal
queue (its size is set with `--limit` option). While buffering messages for
AMQP, piping to the stdout will not block and continue at usual pace because it's
executed in a separate thread.

When the internal queue is filled up it will drop new lines from buffering for
AMQP broker but piping to stdout will continue to work. In this case it will
print the log message

    $ linegen | teemq -e logs -q stream -k us-east > /dev/null
    2017-11-19 00:38:04: [Tee]: Dropping line because QUEUE IS FULL
    ...
