from src.jobs import read


def get_unique_job_types(path):
    jobs = read(path)
    uniqueJobTypes = []
    for type in jobs:
        if type["job_type"] not in uniqueJobTypes:
            uniqueJobTypes.append(type["job_type"])
    return uniqueJobTypes


def filter_by_job_type(jobs, job_type):
    filteredJobs = []
    for jobType in jobs:
        if jobType["job_type"] == job_type:
            filteredJobs.append(jobType)
    return filteredJobs
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    return []


def get_unique_industries(path):
    jobs = read(path)
    uniqueIndustries = []
    for industry in jobs:
        if (
            industry["industry"] not in uniqueIndustries
            and industry["industry"] != ""
        ):
            uniqueIndustries.append(industry["industry"])
    return uniqueIndustries


def filter_by_industry(jobs, industry):
    filteredJobs = []
    for industryType in jobs:
        if industryType["industry"] == industry:
            filteredJobs.append(industryType)
    return filteredJobs

    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    return []


def get_max_salary(path):
    jobs = read(path)
    maxSalary = 0
    for salary in jobs:
        if salary["max_salary"].isnumeric() and int(
            salary["max_salary"]
        ) > int(maxSalary):
            maxSalary = int(salary["max_salary"])
    return maxSalary


def get_min_salary(path):
    jobs = read(path)
    minSalary = get_max_salary(path)
    for salary in jobs:
        if salary["min_salary"].isnumeric() and int(
            salary["min_salary"]
        ) < int(minSalary):
            minSalary = int(salary["min_salary"])
    return minSalary


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
