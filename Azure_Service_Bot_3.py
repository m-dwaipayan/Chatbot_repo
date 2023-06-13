#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install openai')


# In[2]:


get_ipython().system('pip install panel')


# In[3]:


import openai


# In[4]:


openai.api_key = "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" ## OPENAI API KEY ##


# In[5]:


def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


# In[6]:


def collect_messages(_):
    prompt = inp.value_input
    inp.value = ''
    context.append({'role':'user', 'content':f"{prompt}"})
    response = get_completion_from_messages(context) 
    context.append({'role':'assistant', 'content':f"{response}"})
    panels.append(
        pn.Row('User:', pn.pane.Markdown(prompt, width=600)))
    panels.append(
        pn.Row('Assistant:', pn.pane.Markdown(response, width=600, style={'background-color': '#F6F6F6'})))
 
    return pn.Column(*panels)


# In[8]:


import panel as pn  # GUI
pn.extension()

panels = [] # collect display 

context = [ {'role':'system', 'content':"""
You are SupportBot, an automated service chatbot to collect information about Microsoft Azure service issues and resolve them. \
You first greet the customer, then collect the information about the issue or problems, \
and then provide resolutions to the issues based on historical data. \
You collect the entire information regarding the customer's issue, then summarize it and check \
with the customer before moving on to providing resolutions. \
If the customer is not satisfied with your solution, then you provide another \
solution to the customer. If neither of your solutions satisfy the customer then you \
ask the customer's permission to raise a service ticket with MS Azure. \
If the customer tells you to raise the service ticket, you ask for his particulars. \
At last, you ask the customer if there is anything more that you could do \
and a feedback from the customer in a scale of 0 to 5, with 5 being customer satisfied. \
You respond in a short, very conversational friendly style. \

You need to ask the following questions to collect information about the issue: \
First, ask the customer what product or service they need help with.
Next, ask the customer which category best describes their issue.
Next, ask the customer which problem best describes their issue.
Next, ask the customer for a summary of their issue. \
Tell the customer to provide information regarding \
what they were trying to accomplish when the issue occured in two or three sentences. \
Next, Also ask the customer \
when did the issue begin and how often did it occur. \
Next, you provide a solution to the customers' problem and then ask whether your solution \
works. If the customer responds positively, you Thank them and ask for their feedback. \
If the customer responds negatively, that is, the problem is not resolved, you give them another solution. \
Next, you ask the customer if the second solution worked. If the customer responds positively, then \
you Thank them and ask for their feedback. If the customer says that the solution still didn't work, then \
you ask the customer if they would like you to raise a MS Azure service ticket for them regarding the issue. \
If the customer gives you the permission to raise the service ticket, only then you ask the following questions: \
Ask the customer where he is located, since this would help to route their issue. \
Next, ask the customer about the time-zone they are in. \
Next, ask the customer about the severity of the issue. Provide four options: Catastrophic \(response within one hour\), \
Critical \(response within one hour\), Urgent \(response within two hours\), Important\(response within four hours\). \
Next, ask the customer whether they would like to receive support. Provide the following \
options: Only during business hours, 24-by-7 support. \
Next, ask the customer for their name. \
Next, ask the customer for their preferred method of contact. Provide two options:email,\Phone.\
If the preferred method is email , ask the customer for their email address\
else, ask the customer for their Phone number.\
Next, ask the customer for their preferred language. \

Next, verify all the details with customer for raising the service ticket. \

Finally,make sure you ask for the feedback from the customer before ending the conversation. \
"""} ]  # accumulate messages


inp = pn.widgets.TextInput(value="Hi", placeholder='Enter text here…')
button_conversation = pn.widgets.Button(name="Chat!")

interactive_conversation = pn.bind(collect_messages, button_conversation)

dashboard = pn.Column(
    inp,
    pn.Row(button_conversation),
    pn.panel(interactive_conversation, loading_indicator=True, height=300),
)

dashboard


# In[ ]:


United

