from services.contact_service import ContactService
from views.contact_view import ContactView


def main() -> None:
    service = ContactService()
    view = ContactView(service)
    view.run()


if __name__ == "__main__":
    main()
