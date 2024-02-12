#!/usr/bin/python

import json
from types import NoneType
from typing import List, Any, Union, Dict, Type, cast

import attr
import pyalpm
import requests
from pycman import config


@attr.s(auto_attribs=True)
class PackageBasic:
    id: Union[None, int] = None
    name: Union[None, str] = None
    description: Union[None, None, str] = None
    package_base_id: Union[None, int] = None
    package_base: Union[None, str] = None
    maintainer: Union[None, None, str] = None
    num_votes: Union[None, int] = None
    popularity: Union[None, float] = None
    first_submitted: Union[None, int] = None
    last_modified: Union[None, int] = None
    out_of_date: Union[None, None, str] = None
    version: Union[None, str] = None
    url_path: Union[None, None, str] = None
    url: Union[None, None, str] = None
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        description = self.description
        package_base_id = self.package_base_id
        package_base = self.package_base
        maintainer = self.maintainer
        num_votes = self.num_votes
        popularity = self.popularity
        first_submitted = self.first_submitted
        last_modified = self.last_modified
        out_of_date = self.out_of_date
        version = self.version
        url_path = self.url_path
        url = self.url
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not None:
            field_dict["ID"] = id
        if name is not None:
            field_dict["Name"] = name
        if description is not None:
            field_dict["Description"] = description
        if package_base_id is not None:
            field_dict["PackageBaseID"] = package_base_id
        if package_base is not None:
            field_dict["PackageBase"] = package_base
        if maintainer is not None:
            field_dict["Maintainer"] = maintainer
        if num_votes is not None:
            field_dict["NumVotes"] = num_votes
        if popularity is not None:
            field_dict["Popularity"] = popularity
        if first_submitted is not None:
            field_dict["FirstSubmitted"] = first_submitted
        if last_modified is not None:
            field_dict["LastModified"] = last_modified
        if out_of_date is not None:
            field_dict["OutOfDate"] = out_of_date
        if version is not None:
            field_dict["Version"] = version
        if url_path is not None:
            field_dict["URLPath"] = url_path
        if url is not None:
            field_dict["URL"] = url
        return field_dict

    @classmethod
    def from_dict(cls: Type["PackageBasic"], src_dict: Dict[str, Any]) -> "PackageBasic":
        d = src_dict.copy()
        id = d.pop("ID", None)
        name = d.pop("Name", None)
        description = d.pop("Description", None)
        package_base_id = d.pop("PackageBaseID", None)
        package_base = d.pop("PackageBase", None)
        maintainer = d.pop("Maintainer", None)
        num_votes = d.pop("NumVotes", None)
        popularity = d.pop("Popularity", None)
        first_submitted = d.pop("FirstSubmitted", None)
        last_modified = d.pop("LastModified", None)
        out_of_date = d.pop("OutOfDate", None)
        version = d.pop("Version", None)
        url_path = d.pop("URLPath", None)
        url = d.pop("URL", None)
        package_basic = cls(
            id=id,
            name=name,
            description=description,
            package_base_id=package_base_id,
            package_base=package_base,
            maintainer=maintainer,
            num_votes=num_votes,
            popularity=popularity,
            first_submitted=first_submitted,
            last_modified=last_modified,
            out_of_date=out_of_date,
            version=version,
            url_path=url_path,
            url=url,
        )
        package_basic.additional_properties = d
        return package_basic

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties


@attr.s(auto_attribs=True)
class SearchResult:
    resultcount: Union[None, int] = None
    type: Union[None, str] = None
    version: Union[None, int] = None
    results: Union[None, List["PackageBasic"]] = None
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        resultcount = self.resultcount
        type = self.type
        version = self.version
        results: Union[None, List[Dict[str, Any]]] = None
        if not isinstance(self.results, NoneType):
            results = []
            for results_item_data in self.results:
                results_item = results_item_data.to_dict()
                results.append(results_item)
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if resultcount is not None:
            field_dict["resultcount"] = resultcount
        if type is not None:
            field_dict["type"] = type
        if version is not None:
            field_dict["version"] = version
        if results is not None:
            field_dict["results"] = results
        return field_dict

    @classmethod
    def from_dict(cls: Type["SearchResult"], src_dict: Dict[str, Any]) -> "SearchResult":
        d = src_dict.copy()
        resultcount = d.pop("resultcount", None)
        type = d.pop("type", None)
        version = d.pop("version", None)
        results = []
        _results = d.pop("results", None)
        for results_item_data in _results or []:
            results_item = PackageBasic.from_dict(results_item_data)
            results.append(results_item)
        search_result = cls(
            resultcount=resultcount,
            type=type,
            version=version,
            results=results,
        )
        search_result.additional_properties = d
        return search_result

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties


@attr.s(auto_attribs=True)
class PackageDetailed:
    id: Union[None, int] = None
    name: Union[None, str] = None
    description: Union[None, None, str] = None
    package_base_id: Union[None, int] = None
    package_base: Union[None, str] = None
    maintainer: Union[None, None, str] = None
    num_votes: Union[None, int] = None
    popularity: Union[None, float] = None
    first_submitted: Union[None, int] = None
    last_modified: Union[None, int] = None
    out_of_date: Union[None, None, str] = None
    version: Union[None, str] = None
    url_path: Union[None, None, str] = None
    url: Union[None, None, str] = None
    submitter: Union[None, str] = None
    license_: Union[None, List[str]] = None
    depends: Union[None, List[str]] = None
    make_depends: Union[None, List[str]] = None
    opt_depends: Union[None, List[str]] = None
    check_depends: Union[None, List[str]] = None
    provides: Union[None, List[str]] = None
    conflicts: Union[None, List[str]] = None
    replaces: Union[None, List[str]] = None
    groups: Union[None, List[str]] = None
    keywords: Union[None, List[str]] = None
    co_maintainers: Union[None, List[str]] = None
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        description = self.description
        package_base_id = self.package_base_id
        package_base = self.package_base
        maintainer = self.maintainer
        num_votes = self.num_votes
        popularity = self.popularity
        first_submitted = self.first_submitted
        last_modified = self.last_modified
        out_of_date = self.out_of_date
        version = self.version
        url_path = self.url_path
        url = self.url
        submitter = self.submitter
        license_: Union[None, List[str]] = None
        if not isinstance(self.license_, NoneType):
            license_ = self.license_
        depends: Union[None, List[str]] = None
        if not isinstance(self.depends, NoneType):
            depends = self.depends
        make_depends: Union[None, List[str]] = None
        if not isinstance(self.make_depends, NoneType):
            make_depends = self.make_depends
        opt_depends: Union[None, List[str]] = None
        if not isinstance(self.opt_depends, NoneType):
            opt_depends = self.opt_depends
        check_depends: Union[None, List[str]] = None
        if not isinstance(self.check_depends, NoneType):
            check_depends = self.check_depends
        provides: Union[None, List[str]] = None
        if not isinstance(self.provides, NoneType):
            provides = self.provides
        conflicts: Union[None, List[str]] = None
        if not isinstance(self.conflicts, NoneType):
            conflicts = self.conflicts
        replaces: Union[None, List[str]] = None
        if not isinstance(self.replaces, NoneType):
            replaces = self.replaces
        groups: Union[None, List[str]] = None
        if not isinstance(self.groups, NoneType):
            groups = self.groups
        keywords: Union[None, List[str]] = None
        if not isinstance(self.keywords, NoneType):
            keywords = self.keywords
        co_maintainers: Union[None, List[str]] = None
        if not isinstance(self.co_maintainers, NoneType):
            co_maintainers = self.co_maintainers
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not None:
            field_dict["ID"] = id
        if name is not None:
            field_dict["Name"] = name
        if description is not None:
            field_dict["Description"] = description
        if package_base_id is not None:
            field_dict["PackageBaseID"] = package_base_id
        if package_base is not None:
            field_dict["PackageBase"] = package_base
        if maintainer is not None:
            field_dict["Maintainer"] = maintainer
        if num_votes is not None:
            field_dict["NumVotes"] = num_votes
        if popularity is not None:
            field_dict["Popularity"] = popularity
        if first_submitted is not None:
            field_dict["FirstSubmitted"] = first_submitted
        if last_modified is not None:
            field_dict["LastModified"] = last_modified
        if out_of_date is not None:
            field_dict["OutOfDate"] = out_of_date
        if version is not None:
            field_dict["Version"] = version
        if url_path is not None:
            field_dict["URLPath"] = url_path
        if url is not None:
            field_dict["URL"] = url
        if submitter is not None:
            field_dict["Submitter"] = submitter
        if license_ is not None:
            field_dict["License"] = license_
        if depends is not None:
            field_dict["Depends"] = depends
        if make_depends is not None:
            field_dict["MakeDepends"] = make_depends
        if opt_depends is not None:
            field_dict["OptDepends"] = opt_depends
        if check_depends is not None:
            field_dict["CheckDepends"] = check_depends
        if provides is not None:
            field_dict["Provides"] = provides
        if conflicts is not None:
            field_dict["Conflicts"] = conflicts
        if replaces is not None:
            field_dict["Replaces"] = replaces
        if groups is not None:
            field_dict["Groups"] = groups
        if keywords is not None:
            field_dict["Keywords"] = keywords
        if co_maintainers is not None:
            field_dict["CoMaintainers"] = co_maintainers
        return field_dict

    @classmethod
    def from_dict(cls: Type["PackageDetailed"], src_dict: Dict[str, Any]) -> "PackageDetailed":
        d = src_dict.copy()
        id = d.pop("ID", None)
        name = d.pop("Name", None)
        description = d.pop("Description", None)
        package_base_id = d.pop("PackageBaseID", None)
        package_base = d.pop("PackageBase", None)
        maintainer = d.pop("Maintainer", None)
        num_votes = d.pop("NumVotes", None)
        popularity = d.pop("Popularity", None)
        first_submitted = d.pop("FirstSubmitted", None)
        last_modified = d.pop("LastModified", None)
        out_of_date = d.pop("OutOfDate", None)
        version = d.pop("Version", None)
        url_path = d.pop("URLPath", None)
        url = d.pop("URL", None)
        submitter = d.pop("Submitter", None)
        license_ = cast(List[str], d.pop("License", None))
        depends = cast(List[str], d.pop("Depends", None))
        make_depends = cast(List[str], d.pop("MakeDepends", None))
        opt_depends = cast(List[str], d.pop("OptDepends", None))
        check_depends = cast(List[str], d.pop("CheckDepends", None))
        provides = cast(List[str], d.pop("Provides", None))
        conflicts = cast(List[str], d.pop("Conflicts", None))
        replaces = cast(List[str], d.pop("Replaces", None))
        groups = cast(List[str], d.pop("Groups", None))
        keywords = cast(List[str], d.pop("Keywords", None))
        co_maintainers = cast(List[str], d.pop("CoMaintainers", None))
        package_detailed = cls(
            id=id,
            name=name,
            description=description,
            package_base_id=package_base_id,
            package_base=package_base,
            maintainer=maintainer,
            num_votes=num_votes,
            popularity=popularity,
            first_submitted=first_submitted,
            last_modified=last_modified,
            out_of_date=out_of_date,
            version=version,
            url_path=url_path,
            url=url,
            submitter=submitter,
            license_=license_,
            depends=depends,
            make_depends=make_depends,
            opt_depends=opt_depends,
            check_depends=check_depends,
            provides=provides,
            conflicts=conflicts,
            replaces=replaces,
            groups=groups,
            keywords=keywords,
            co_maintainers=co_maintainers,
        )
        package_detailed.additional_properties = d
        return package_detailed

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties


@attr.s(auto_attribs=True)
class InfoResult:
    resultcount: Union[None, int] = None
    type: Union[None, str] = None
    version: Union[None, int] = None
    results: Union[None, List["PackageDetailed"]] = None
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        resultcount = self.resultcount
        type = self.type
        version = self.version
        results: Union[None, List[Dict[str, Any]]] = None
        if not isinstance(self.results, NoneType):
            results = []
            for results_item_data in self.results:
                results_item = results_item_data.to_dict()
                results.append(results_item)
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if resultcount is not None:
            field_dict["resultcount"] = resultcount
        if type is not None:
            field_dict["type"] = type
        if version is not None:
            field_dict["version"] = version
        if results is not None:
            field_dict["results"] = results
        return field_dict

    @classmethod
    def from_dict(cls: Type["InfoResult"], src_dict: Dict[str, Any]) -> "InfoResult":
        d = src_dict.copy()
        resultcount = d.pop("resultcount", None)
        type = d.pop("type", None)
        version = d.pop("version", None)
        results = []
        _results = d.pop("results", None)
        for results_item_data in _results or []:
            results_item = PackageDetailed.from_dict(results_item_data)
            results.append(results_item)
        info_result = cls(
            resultcount=resultcount,
            type=type,
            version=version,
            results=results,
        )
        info_result.additional_properties = d
        return info_result

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties


handle = None
aur_url = "https://aur.archlinux.org/rpc/v5"

local_repos = ["custom", "loathk-public", "loathk-personal"]
arch_repos = ["core", "extra", "community", "multilib"]


def search_single(name: str):
    response = requests.get(f"{aur_url}/search/{name}?by=name")
    return SearchResult.from_dict((json.loads(response.content)))


def info_multiple(names: List[str]):
    payload = {"arg[]": names}
    response = requests.get(f"{aur_url}/info", params=payload)
    return InfoResult.from_dict(json.loads(response.content))


if __name__ == "__main__":
    handle = config.init_with_config("/etc/pacman.conf")
    arch_dbs = list(filter(
        lambda r: r.name in arch_repos,
        [db for db in handle.get_syncdbs()]
    ))

    local_dbs = list(filter(
        lambda r: r.name in local_repos,
        [db for db in handle.get_syncdbs()]
    ))

    for ldb in local_dbs:
        local_packages: List[pyalpm.Package] = ldb.search("")
        local_packages = sorted(local_packages, key=lambda p: p.db.name)
        for lp in local_packages:
            for adb in arch_dbs:
                ap = adb.get_pkg(lp.name)
                if ap is not None:
                    # vercmp: left > right = 1
                    # vercmp: left < right = -1
                    outdated = pyalpm.vercmp(lp.version, ap.version)
                    if outdated < 0:
                        print("{:16s} {} {}".format(adb.name, lp.name, lp.version))
                        print("{:16s} Newer version in {}: {}".format("", adb.name, ap.version))
                    local_packages.remove(lp)

        local_packages = sorted(local_packages, key=lambda p: p.name)
        aur_info = info_multiple([lp.name for lp in local_packages])
        aur_packages = sorted(aur_info.results, key=lambda p: p.name)
        local_aur_packages = [lp for lp in local_packages if lp.name in [ap.name for ap in aur_packages]]
        for lp, ap in zip(local_aur_packages, aur_packages):
            if ap.name == lp.name:
                outdated = pyalpm.vercmp(lp.version, ap.version)
                if outdated < 0:
                    print("{:16s} {} {}".format(f"AUR - {ldb.name}", lp.name, lp.version))
                    print("{:16s} Newer version in {}: {}".format("", "AUR", ap.version))

        local_non_aur_packages = [lp for lp in local_packages if lp.name not in [ap.name for ap in aur_packages]]
        for lnap in local_non_aur_packages:
            print("{:16s} {}".format(f"NON - {ldb.name}", lnap.name))
