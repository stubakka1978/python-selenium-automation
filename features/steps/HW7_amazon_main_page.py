from behave import when


@when('Click Returns & Orders')
def click_signin_button(context):
    context.app.sign_in_page.click_signin_button()


@when('Click Cart')
def click_cart_button(context):
    context.app.cart_page.click_cart_button()