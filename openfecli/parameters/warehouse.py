from plugcli.params import Option


WAREHOUSE = Option(
    "-w",
    "--warehouse",
    help="Enable experimental warehouse output support",
    is_flag=True,
    default=False,
)
