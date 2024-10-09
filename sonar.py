from sonarqube import SonarQubeClient


def getSonarqubeInfo(branch="master", component=None, url=None, username=None, password=None):
    sonar = SonarQubeClient(sonarqube_url=url,username=username,password=password)
    component_data = sonar.measures.get_component_with_specified_measures(
        component=component,
        branch=branch,
        fields="metrics,periods",
        metricKeys="""
        code_smells,bugs,coverage,duplicated_lines_density,ncloc,
        security_rating,reliability_rating,vulnerabilities,comment_lines_density,
        ncloc_language_distribution,alert_status,sqale_rating
        """
    )

    result_dict = {}
    for info_dict in component_data["component"]["measures"]:
        result_dict[info_dict["metric"]] = info_dict["value"]

    return result_dict
