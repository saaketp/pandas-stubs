"""
This class could be comprehensibly typed with the typeshed .pyi file but the
datatetime.datetime and pd.Timestamp API differ quite a bit and cannot be used interchangeably
"""
import sys
from typing import Any, Optional, Union, overload, TypeVar, Type

from pandas._libs.tslibs.timedeltas import Timedelta

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

from dateutil.tz import tzfile
from datetime import tzinfo, datetime, date as _date, time, timedelta

from pandas._libs.tslibs.period import Period
from pandas._typing import TimestampConvertible

OptInt = Optional[int]

Fold = Literal[0, 1]

_S = TypeVar("_S")

class Timestamp(datetime):
    @overload
    def __init__(self, ts_input: TimestampConvertible, freq: Optional[str] = ..., tz: Optional[Union[str, tzinfo, tzfile]] = ...,
                 unit: Optional[str] = ..., tzinfo: Optional[tzinfo] = ..., fold: Optional[Fold] = ...): ...
    @overload
    def __init__(self, year: OptInt = ..., month: OptInt = ..., day: OptInt = ..., hour: OptInt = ..., minute: OptInt = ...,
                 second: OptInt = ..., microsecond: OptInt = ..., nanosecond: OptInt = ..., tz: Optional[Union[str, tzinfo, tzfile]] = ...,
                 tzinfo: Optional[tzinfo] = ..., fold: Optional[Fold] = ..., freq: Optional[str] = ...): ...
    def to_period(self, freq: Optional[str]) -> Period: ...
    def to_julian_date(self) -> float: ...
    def tz_localize(self, tz: Any = ..., ambigious: Any = ..., nonexistent: Any = ...) -> Timestamp: ...
    def tz_convert(self, tz: Any) -> Timestamp: ...
    @overload  # type: ignore[override]
    def __sub__(self, other: datetime) -> Timedelta: ...
    @overload
    def __sub__(self, other: timedelta) -> Timestamp: ...
    def __add__(self, other: timedelta) -> Timestamp: ...
    if sys.version_info >= (3, 8):
        def astimezone(self: _S, tz: Optional[tzinfo] = ...) -> _S: ...
    else:
        def astimezone(self, tz: Optional[tzinfo] = ...) -> datetime: ...
    # This is correct. Typeshed doesn't include Optionals, or the Literal correctly
    def replace(self, year: OptInt = ..., month: OptInt = ..., # type: ignore[override]
                day: OptInt = ..., hour: OptInt = ..., minute: OptInt = ...,
                second: OptInt = ..., microsecond: OptInt = ..., nanosecond: OptInt = ...,
                tzinfo: Optional[tzinfo] = ..., *, fold: Fold = ...) -> datetime: ...
    def round(self, freq: str, ambiguous: Any = ..., nonexistent: Any = ...) -> Timestamp: ...
    def ceil(self, freq: str, ambiguous: Any = ..., nonexistent: Any = ...) -> Timestamp: ...
    def floor(self, freq: str, ambiguous: Any = ..., nonexistent: Any = ...) -> Timestamp: ...
    def isoformat(self, sep: str = ..., timespec: str = ...) -> str: ...
    def day_name(self, locale: Optional[str]) -> str: ...
    def month_name(self, locale: Optional[str]) -> str: ...
    def normalize(self) -> Timestamp: ...
    def strftime(self, format: str) -> str: ...
    def date(self) -> _date: ...
    @classmethod
    def utcnow(cls) -> Timestamp: ...
    @classmethod
    def utcfromtimestamp(cls, ts: float) -> Timestamp: ...
    # Pandas doesn't accept timezone here, unlike datetime
    @classmethod
    def fromtimestamp(cls: Type[_S], t: float) -> _S: ... # type: ignore[override]
    @classmethod
    def combine(cls, date: _date, time: time, tzinfo: Optional[tzinfo] = ...) -> Timestamp: ...
    @classmethod
    def now(cls, tz: Optional[Any] = ...) -> Timestamp: ...
    @classmethod
    def today(cls, tz: Optional[Any] = ...) -> Timestamp: ...
    @classmethod
    def fromisoformat(cls, isoformat: str) -> Timestamp: ...
    @classmethod
    def fromordinal(cls, ordinal: Any, freq: Optional[Any] = ..., tz: Optional[Any] = ...) -> Timestamp: ...
    @property
    def dayofweek(self) -> int: ...
    @property
    def dayofyear(self) -> int: ...
    @property
    def quarter(self) -> int: ...
    @property
    def days_in_month(self) -> int: ...
    @property
    def daysinmonth(self) -> int: ...
    @property
    def week(self) -> int: ...
    @property
    def weekofyear(self) -> int: ...
    @property
    def freqstr(self) -> str: ...
    @property
    def is_month_end(self) -> bool: ...
    @property
    def is_month_start(self) -> bool: ...
    @property
    def is_quarter_start(self) -> bool: ...
    @property
    def is_quarter_end(self) -> bool: ...
    @property
    def is_year_start(self) -> bool: ...
    @property
    def is_year_end(self) -> bool: ...
    @property
    def is_leap_year(self) -> bool: ...
    @property
    def tz(self) -> tzinfo: ...


def integer_op_not_supported(obj: Any) -> Any: ...
