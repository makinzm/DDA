from typing import Optional

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import datetime
import pandas as pd
from pandas.core.indexes.datetimes import DatetimeIndex

def draw_aim(start_date: datetime.date, total_pages: int, pages_per_day_goal: int, save_path: Optional[str]=None) -> None:
    days_to_goal: int = total_pages / pages_per_day_goal
    goal_date: datetime.date = start_date + datetime.timedelta(days=days_to_goal)
    dates = pd.date_range(start=start_date, end=goal_date, freq='D')
    fig: Figure
    ax: Axes
    fig, ax = plt.subplots()
    ax.plot(dates, [pages_per_day_goal * (len(dates)-1 -i) for i in range(len(dates))], 'r-', label='Aim')
    ax.set_xlabel('date')
    ax.set_ylabel('pages')
    ax.set_title('Reading Aim, Goal Date: ' + goal_date.strftime("%m/%d/%Y"))
    ax.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    if save_path is not None:
        plt.savefig(save_path)
    plt.show()

if __name__ == "__main__":
    draw_aim(datetime.date.today(), 590, 10, "../../../tmp_files/aim.draw_aim.png")
