from .dns_lookup import lookup, SRVQueryFailure

__all__ = ['resolve']


def resolve(host, template, domain='service.consul', fail_silently=False):
    """
    Queries accessible DNS servers for SRV records with match `host`.`domain`
    Interpolates the result with `template` to generate the connection string.

    Expects that hosts exist on the `service.consul` domain
    e.g. redis.service.consul
    This can be overridden using the domain kwarg

    Example:

    print resolve('mongo-repl', 'mongodb://{}/reservoir?replSet=meh')
    => mongodb://1.1.1.1:1111,2.2.2.2:2222,3.3.3.3:3333/db?replSet=rs

    """
    query = '{0}.{1}'.format(host, domain)
    try:
        hosts = lookup(host, domain=domain)

        return template.format(','.join([
            '{host}:{port}'.format(**x.__dict__) for x in hosts]))

    except SRVQueryFailure:
        if fail_silently:
            return None

        raise SRVQueryFailure('{0} could not be located'.format(query))
