"""Console script for wangls."""
import sys
import click
from terminaltables import SingleTable

from wangls.wangls import is_nmap_installed, get_ips_and_os, get_local_ips


@click.command()
@click.option("--o", "-o", is_flag=True, help="Enable OS detection")
def main(o):
    """A command line tool that gives you the IPs of the devices connected to the same network segment."""
    HEADERS = ["IPs", "MAC Address", "Operating System"]
    if not is_nmap_installed():
        click.echo("Nmap is not installed. Please download Nmap https://nmap.org/download.html")
        return
    if o:
        os_output = get_ips_and_os()
        os_output.insert(0, HEADERS)
        os_table = SingleTable(os_output)
        os_table.inner_row_border = True
        click.echo(os_table.table)
        sys.exit()

    simple_output = get_local_ips()
    simple_output.insert(0, ["IPs"])
    simple_table = SingleTable(simple_output)
    simple_table.inner_row_border = True
    click.echo(simple_table.table)


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
