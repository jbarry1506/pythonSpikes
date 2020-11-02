import jenkinsapi, pprint
import vars

server = jenkinsapi.Jenkins(vars.jenkins_server, username=vars.jenkins_user, password=vars.xv)
pprint.pprint(server.get_all_jobs())