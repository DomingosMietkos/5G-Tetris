from behave import given, when, then

@given('użytkownik chce przetłumaczyć tekst "{original_text}"')
def step_given_user_wants_to_translate_text(context, original_text):
    context.original_text = original_text

@when('uzyskuje tłumaczenie "{translated_text}"')
def step_when_user_gets_translation(context, translated_text):
    context.translated_text = translated_text

@then('uzyskuje tłumaczenie "Witaj, Świecie!"')
def step_then_user_gets_translation(context):
    assert context.translated_text == "Witaj, Świecie!"
