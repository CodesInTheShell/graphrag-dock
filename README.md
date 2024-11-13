## Getting started
- See the docker-compose.yml and update the environment for `GRAPHRAG_API_KEY`
- run by `docker compose up`

API usage
- Initialize by GET http://127.0.0.1:5000/initialize
- Upload the file POST http://127.0.0.1:5000/upload ( can use the book-trimmed.txt )
- Create index by GET http://127.0.0.1:5000/index
- Run query by POST http://127.0.0.1:5000/query
{
    "method": "local",
    "query": "Who is Scrooge and what are his main relationships?"
}

## Some stuff changed
- In settings.yaml model changed to gpt-4o-mini 
- You may need to create a folder on the same directory called `ragtest` maybe with a child folder `input`

### Sample query
{
    "method": "local",
    "query": "Who is Scrooge and what are his main relationships?"
}

### Sample result
{
  "result": "INFO: Vector Store Args: {\n    \"type\": \"lancedb\",\n    \"db_uri\": \"/app/ragtest/output/lancedb\",\n    \"container_name\": \"==== REDACTED ====\",\n    \"overwrite\": true\n}\ncreating llm client with {'api_key': 'REDACTED,len=164', 'type': \"openai_chat\", 'model': 'gpt-4-turbo-preview', 'max_tokens': 4000, 'temperature': 0.0, 'top_p': 1.0, 'n': 1, 'request_timeout': 180.0, 'api_base': None, 'api_version': None, 'organization': None, 'proxy': None, 'audience': None, 'deployment_name': None, 'model_supports_json': True, 'tokens_per_minute': 0, 'requests_per_minute': 0, 'max_retries': 10, 'max_retry_wait': 10.0, 'sleep_on_rate_limit_recommendation': True, 'concurrent_requests': 25}\ncreating embedding llm client with {'api_key': 'REDACTED,len=164', 'type': \"openai_embedding\", 'model': 'text-embedding-3-small', 'max_tokens': 4000, 'temperature': 0, 'top_p': 1, 'n': 1, 'request_timeout': 180.0, 'api_base': None, 'api_version': None, 'organization': None, 'proxy': None, 'audience': None, 'deployment_name': None, 'model_supports_json': None, 'tokens_per_minute': 0, 'requests_per_minute': 0, 'max_retries': 10, 'max_retry_wait': 10.0, 'sleep_on_rate_limit_recommendation': True, 'concurrent_requests': 25}\n\nSUCCESS: Local Search Response:\n### Overview of Scrooge\n\nEbenezer Scrooge, the central character of Charles Dickens' \"A Christmas Carol,\" is depicted as a miserly old man, known for his squeezing, wrenching, grasping, scraping, clutching, covetous old sinner demeanor. He is characterized by his cold demeanor, which affects not only his physical appearance but also his social interactions, making him a solitary figure who expresses disdain for Christmas and its celebrations. Throughout the story, Scrooge is visited by spirits showing him past, present, and future events to reflect on his life choices and attitudes towards wealth and happiness, leading him towards redemption [Data: Entities (26)].\n\n### Scrooge's Main Relationships\n\n#### Fezziwig\nFezziwig is a key figure from Scrooge's past, serving as his former employer and mentor during his apprenticeship. Scrooge remembers Fezziwig with great fondness and excitement, highlighting Fezziwig's jovial and generous nature. This relationship is crucial in illustrating the contrast between Scrooge's current miserliness and the potential for joy and generosity he once knew [Data: Relationships (45, 22); Entities (41)].\n\n#### Fan\nFan is Scrooge's younger sister, who is depicted as having a large heart and bringing Scrooge home for Christmas in their youth. Despite dying young, Fan's character embodies warmth and familial love, contrasting sharply with Scrooge's cold demeanor. Her significance lies in her role as the mother of Scrooge's nephew, further linking Scrooge to his family [Data: Relationships (28); Entities (23)].\n\n#### Scrooge's Nephew\nScrooge's nephew represents the spirit of Christmas with his optimistic outlook and charitable nature. He stands in stark contrast to Scrooge's initial miserly demeanor, embodying the themes of generosity, warmth, and community spirit that Scrooge initially refuses to embrace. The nephew's persistent attempts to connect with Scrooge, inviting him to dine and share in the Christmas cheer, highlight the familial bond and the potential for Scrooge's transformation [Data: Relationships (36, 32); Entities (31, 27)].\n\n#### Bob Cratchit\nBob Cratchit, Scrooge's clerk, is another significant relationship in Scrooge's life. Despite his low wages and poor working conditions, Cratchit celebrates Christmas, embodying the holiday's spirit of hope and kindness. Scrooge's interactions with Cratchit, particularly his initial refusal to provide adequate warmth and his threat of job loss for celebrating Christmas, serve as a reflection of Scrooge's miserliness and eventual change of heart [Data: Relationships (33, 37); Entities (9, 28)].\n\n#### Jacob Marley\nJacob Marley, Scrooge's former business partner, appears as a spectre warning Scrooge of the visitation by three spirits and urging him to change his ways. This relationship is pivotal as it sets the stage for Scrooge's journey of self-reflection and redemption. Marley's fate serves as a cautionary tale for Scrooge, highlighting the consequences of a life lived without generosity or compassion [Data: Relationships (38, 40); Entities (14, 35)].\n\n### Conclusion\n\nScrooge's relationships are central to his character development in \"A Christmas Carol.\" They serve as mirrors reflecting his flaws and opportunities for growth, as well as catalysts for his eventual transformation. Through interactions with figures like Fezziwig, Fan, his nephew, Bob Cratchit, and Jacob Marley, Scrooge is led to reevaluate his life and priorities, ultimately embracing the true spirit of Christmas."
}

### Youtube video
- https://youtu.be/E1tB9ka4N0E

## Python troubleshooting
### Remove 3.13
sudo apt remove python3.13 python3.13-dev python3.13-minimal

### installed 3.12
sudo apt install python3.12 python3.12-dev python3.12-minimal

### create a virtualenv
virtualenv -p python3.12 venv

### if you are getting issue with pip when running pip commands 
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3.12 get-pip.py

### You can set Python 3.12 as the default Python version system-wide
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.12 1
sudo update-alternatives --config python

# This is not ready for production