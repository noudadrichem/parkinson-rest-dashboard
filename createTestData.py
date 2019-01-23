commands = (
'''
CREATE TABLE patient (
  id BIGSERIAL PRIMARY KEY unique,
  fullName varchar(255) not null,
  leeftijd int not null,
  initialDoses varchar(255),
  bodyMass float,
  created date not null default CURRENT_DATE
);
''',
'''CREATE TABLE trillingen (
  id BIGSERIAL PRIMARY KEY unique,
  aantaltrillingen float,
  per varchar(255) default 'halfeminuut',
  created date not null default CURRENT_DATE,
  patientid int REFERENCES patient (id)
);
''',
'''
CREATE TABLE dokter (
  id BIGSERIAL PRIMARY KEY unique,
  fullName varchar(255) not null,
  ziekenhuis int not null,
  created date not null default CURRENT_DATE,
  patientid int REFERENCES patient (id)
);
''',
'''
CREATE TABLE activity (
  id BIGSERIAL PRIMARY KEY unique,
  staje BOOLEAN not null,
  created date not null default CURRENT_DATE,
  patientid int REFERENCES patient (id)
);
'''
)
