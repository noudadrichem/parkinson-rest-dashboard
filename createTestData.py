commands = (
'''
CREATE TABLE patient (
  id BIGSERIAL PRIMARY KEY unique,
  fullname varchar(255) not null,
  leeftijd int not null,
  initialdoses varchar(255),
  bodymass float,
  created date not null default now()
);
''',
'''CREATE TABLE trillingen (
  id BIGSERIAL PRIMARY KEY unique,
  aantaltrillingen float,
  per varchar(255) default 'halfeminuut',
  created varchar(255) not null,
  patientid int REFERENCES patient (id)
);
''',
'''
CREATE TABLE dokter (
  id BIGSERIAL PRIMARY KEY unique,
  fullName varchar(255) not null,
  ziekenhuis varchar(255) not null,
  created date not null default now()
);
''',
'''
CREATE TABLE activity (
  id BIGSERIAL PRIMARY KEY unique,
  staje BOOLEAN not null,
  created varchar(255) not null,
  patientid int REFERENCES patient (id)
);
'''
)
