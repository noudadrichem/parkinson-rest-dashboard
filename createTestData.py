import db
print(db.connection)

commands = (
'''CREATE TABLE IF NOT EXISTS patient (
  id BIGSERIAL PRIMARY KEY unique,
  fullname varchar(255) not null,
  leeftijd int not null,
  initialdoses varchar(255),
  bodymass float,
  created date not null default now()
);
''',
'''CREATE TABLE IF NOT EXISTS trillingen (
  id BIGSERIAL PRIMARY KEY unique,
  aantaltrillingen float,
  per varchar(255) default 'halfeminuut',
  created varchar(255) not null,
  patientid int REFERENCES patient (id)
);
''',
'''CREATE TABLE IF NOT EXISTS dokter (
  id BIGSERIAL PRIMARY KEY unique,
  fullName varchar(255) not null,
  ziekenhuis varchar(255) not null,
  created date not null default now()
);
''',
'''CREATE TABLE IF NOT EXISTS activity (
  id BIGSERIAL PRIMARY KEY unique,
  staje BOOLEAN not null,
  created varchar(255) not null,
  patientid int REFERENCES patient (id)
);
'''
)

def initDatabaseTables():
  cur = db.connection.cursor()

  for command in commands:
    cur.execute(
      command
    )
    print('''
    {}
    '''.format(command))

  cur.close()
  db.connection.commit()

  print('Succesfully created tables.')

# Use this function to initialize the database tables.
initDatabaseTables()
