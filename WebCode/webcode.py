try:
    from PyCLogo.pyclogo import PyCLogo

    from requests import get
except ImportError:
    print('Seem\'s some some dependencies is not installed...')

webcode_logo = PyCLogo()

webcode_logo.update_image("webcode.png")

webcode_logo.add_info("Project Name", "Web Code.")
webcode_logo.add_info("Description", "Get GET code from any web site in few seconds.")
webcode_logo.add_info("Author", "Ivan Perzhynsky.")
webcode_logo.add_info("Version", "1.0")
webcode_logo.add_info("License", "MIT License.")

webcode_logo.print_window("green")

while True:
    web_site = input("Web-site (1 to exit): ")

    if web_site == "1":
        print("Bye!")

        break

    try:
        get_res = get(f'{"https://" if not web_site.startswith("https://") else ""}{web_site}')
    except Exception:
        print('An exception was occured due parsing web site.\n')

        continue

    print(f"Code: {get_res.status_code}.\n")
